# module
name    = "onmyojideckbuilder"
region  = "eu-west-1"
stage   = "prod"
profile = "admin"

# cloudfront
acm_certificate_arn = "arn:aws:acm:us-east-1:745437999005:certificate/11502ff4-7851-426f-92ac-27db7c44825f"
parent_zone_id      = "Z0511918V1SF3MCG22JU"
aliases             = ["onmyojideckbuilder.com"]
allowed_origins     = ["*.onmyojideckbuilder.com"]

# s3 & lambda
acl         = "private"
lambda_key  = "main.zip"
source_file = "./lambda/main.js"
handler     = "main.handler"
runtime     = "nodejs12.x"
s3_region   = "us-east-1"
