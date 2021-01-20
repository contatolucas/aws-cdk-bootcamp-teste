#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_bootcamp_teste.aws_cdk_bootcamp_teste_stack import AwsCdkBootcampTesteStack


app = core.App()
AwsCdkBootcampTesteStack(app, "aws-cdk-bootcamp-teste")

app.synth()
