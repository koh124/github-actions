import boto3
import json
import time

cloudfront = boto3.client('cloudfront')
DISTRIBUTION_ID = 'E2VW1LNFW3XLLZ'
Items = ['/*']

# cloudfrontのキャッシュを削除
def lambdaHandler(event, context):
    cloudfront.create_invalidation(DistributionId=DISTRIBUTION_ID, InvalidationBatch={
        "Paths": {
            "Quantity": len(Items),
            "Items": Items
        },
        "CallerReference": str(time.time())
    })

    return {
        'statusCode': 200,
        'body': "CloudFront cache successfully deleted"
    }
