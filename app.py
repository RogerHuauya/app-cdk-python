#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import DefaultStackSynthesizer
from app_cdk_python.app_cdk_python_stack import AppCdkStack

app = cdk.App()

default_stack_synthesizer = DefaultStackSynthesizer(
    file_assets_bucket_name="cdk-${Qualifier}-assets-${AWS::AccountId}-${AWS::Region}",
    bucket_prefix="",

    image_assets_repository_name="cdk-${Qualifier}-container-assets-${AWS::AccountId}-${AWS::Region}",

    deploy_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/LabRole",
    deploy_role_external_id="",

    file_asset_publishing_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/LabRole",
    file_asset_publishing_external_id="",

    image_asset_publishing_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/LabRole",
    image_asset_publishing_external_id="",

    cloud_formation_execution_role="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/LabRole",

    lookup_role_arn="arn:${AWS::Partition}:iam::${AWS::AccountId}:role/LabRole",
    lookup_role_external_id="",

    bootstrap_stack_version_ssm_parameter="/cdk-bootstrap/${Qualifier}/version",

    generate_bootstrap_version_rule=True,
)

AppCdkStack(app, "AppCdkPythonStack",
    synthesizer=default_stack_synthesizer,
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()