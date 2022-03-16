### This repo provides API to service of shorting url
To use API install requirements, 
run
`export FLASK_APP=url_short`, and then
`flask run`
After that you can make request to your local domain, or if you using some other domain, you can
change it for service in file domains.yaml
Endpoints:
`/api/v1/get_short/?url=URL&exp=EXP_DATE` - create shorted url, with expire date = EXP_DATE, default - 90 days