# Commands

## Adding new cards to json

- Increase prettier line width to 200
- Quote Props to persistent
- Sort lines by natural
- Add `"id": ""`
- Generate GUID and remove the tails

## Deploy to S3

<https://github.com/bep/s3deploy>

### prod

`s3deploy -source=./dist -region=eu-west-1 -bucket=prod-onmyojideckbuilder-origin -distribution-id=E8811LTEVQX71`

### dev

`s3deploy -source=./dist -region=eu-west-1 -bucket=dev-onmyojideckbuilder-origin -distribution-id=E26QN6RRQRWYWL`
