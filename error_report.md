# Error Report

| Test | Error | Reason | Result |
|------|-------|--------|--------|
| Missing MonthlyCharges | 422 Unprocessable Entity | Required field missing | Passed |
| tenure = "abc" | 422 Unprocessable Entity | Invalid integer value | Passed |
| customers = [] | Empty predictions list returned | No customer records provided | Passed |