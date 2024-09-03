from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elbv2,
    CfnOutput,
)
from constructs import Construct

class AppCdkStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self, 'VPC', is_default=True)

        asg = autoscaling.AutoScalingGroup(self, 'MyASG',
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            min_capacity=2,
            role=iam.Role.from_role_arn(self, "ASGExecutionRole", self.get_lab_role_arn())
        )

        alb = elbv2.ApplicationLoadBalancer(self, 'MyALB',
            vpc=vpc,
            internet_facing=True,
        )

        listener = alb.add_listener('HttpListener',
            port=80
        )

        listener.add_targets('Targets',
            port=80,
            targets=[asg]
        )

        listener.connections.allow_default_port_from_any_ipv4(
            'Allow access to port 80 from the internet.')

        CfnOutput(self, 'Hostname', value=alb.load_balancer_dns_name)

    def get_lab_role_arn(self) -> str:
        return self.format_arn(
            service='iam',
            region='',
            account=self.account,
            resource='role/LabRole',
        )