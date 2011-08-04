def buildConnectionString(params):
    """Build a conneciotn string from a dictionary of parameters."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"aa", \
                "pwd":"secret" \
                }
    print buildConnectionString(myParams)
