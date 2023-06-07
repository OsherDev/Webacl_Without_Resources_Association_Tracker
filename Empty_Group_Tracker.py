import boto3
import copy
wafv2_client = boto3.client('wafv2', region_name='us-east-1')
cloudfront_client = boto3.client('cloudfront', region_name='us-east-1')
webACLs = wafv2_client.list_web_acls(Scope="CLOUDFRONT")['WebACLs']

    
def lambda_handler(event, context):
    matches = []
    for webACL in webACLs:
        response = cloudfront_client.list_distributions_by_web_acl_id(WebACLId=webACL['ARN'])
        if response['DistributionList']['Quantity'] == 0:
            matches.append(webACL['ARN'])
    # Print each WebACL group in a new line
    for match in matches:
        print(match)
    # Clear the matches list in each execution
    matches = []
