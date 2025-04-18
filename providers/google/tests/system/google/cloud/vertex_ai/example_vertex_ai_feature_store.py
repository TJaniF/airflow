#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Example Airflow DAG for Google Vertex AI Feature Store operations.
"""

from __future__ import annotations

import os
from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.operators.vertex_ai.feature_store import (
    GetFeatureViewSyncOperator,
    SyncFeatureViewOperator,
)
from airflow.providers.google.cloud.sensors.vertex_ai.feature_store import FeatureViewSyncSensor

PROJECT_ID = os.environ.get("SYSTEM_TESTS_GCP_PROJECT", "default")
DAG_ID = "vertex_ai_feature_store_dag"
REGION = "us-central1"

FEATURE_ONLINE_STORE_ID = "my_feature_online_store_unique"
FEATURE_VIEW_ID = "feature_view_publications"

with DAG(
    dag_id=DAG_ID,
    description="Sample DAG with Vertex AI Feature Store operations.",
    schedule="@once",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example", "vertex_ai", "feature_store"],
) as dag:
    # [START how_to_cloud_vertex_ai_feature_store_sync_feature_view_operator]
    sync_task = SyncFeatureViewOperator(
        task_id="sync_task",
        project_id=PROJECT_ID,
        location=REGION,
        feature_online_store_id=FEATURE_ONLINE_STORE_ID,
        feature_view_id=FEATURE_VIEW_ID,
    )
    # [END how_to_cloud_vertex_ai_feature_store_sync_feature_view_operator]

    # [START how_to_cloud_vertex_ai_feature_store_feature_view_sync_sensor]
    wait_for_sync = FeatureViewSyncSensor(
        task_id="wait_for_sync",
        location=REGION,
        feature_view_sync_name="{{ task_instance.xcom_pull(task_ids='sync_task', key='return_value')}}",
        poke_interval=60,  # Check every minute
        timeout=600,  # Timeout after 10 minutes
        mode="reschedule",
    )
    # [END how_to_cloud_vertex_ai_feature_store_feature_view_sync_sensor]

    # [START how_to_cloud_vertex_ai_feature_store_get_feature_view_sync_operator]
    get_task = GetFeatureViewSyncOperator(
        task_id="get_task",
        location=REGION,
        feature_view_sync_name="{{ task_instance.xcom_pull(task_ids='sync_task', key='return_value')}}",
    )
    # [END how_to_cloud_vertex_ai_feature_store_get_feature_view_sync_operator]

    sync_task >> wait_for_sync >> get_task

    from tests_common.test_utils.watcher import watcher

    # This test needs watcher in order to properly mark success/failure
    # when "tearDown" task with trigger rule is part of the DAG
    list(dag.tasks) >> watcher()

from tests_common.test_utils.system_tests import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
test_run = get_test_run(dag)
