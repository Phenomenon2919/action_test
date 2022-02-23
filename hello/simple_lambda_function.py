from github import Github

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------')

    if event["input"] == "No":
        return "You mean Yes?"
    elif event["input"] == "Yes":
        return "Why though?"
    else:
        raise
