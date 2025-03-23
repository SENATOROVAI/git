def round_value(x):
    """
    Round value 
    
    Args:
        x (float): value

    Returns:
        float: result
    """
    return round(x, 2)


def generateReport(x_list):
    """
    Generate report
    
    Args:
        x_list (list): list of x value

    Returns:
        list: result
    """
    report = []
    
    for i in range(0, len(x_list)):
        x = x_list[i]
        
        result = False
        if x >= 0:
            result = True
        report.append(result)
    
    return report


print(str(round_value(100.2345)))

x_list = [
    -1,
    1
]
report = generateReport(x_list)
print(report)