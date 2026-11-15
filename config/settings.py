AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
TEMP_STS_KEY = "ASIAJ234567890ABCDEF"
GH_CLASSIC_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABCD"
GH_FINE_PAT = "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"
PASSWORD_ADMIN = 'MyAdminPass!987654'

# should be IGNORED (false-positive traps)
aws_key = "0123456789abcdef0123456789abcdef01234567"  # missing 'secret'
password = "process.env.USER_PASSWORD"                # env reference
def github_pat_helper_function():                     # function name, not a token
    pass
