# Swit for Github Action

Send message to Swit with Github Action 

## Inputs

### `webhooks_url`

**Required** Your App's webhooks_url

### `message`

**Required** The message send to swit. Default `"Build Success. ${{ github.sha }}"`

The time we greeted you.

## Example usage

```
uses: actions/action-swit@v1
with:
  webhooks_url: 'https://hook.swit.io/chat/~~~/~~~'
  message: 'Build Success ${{ github.sha	}}
```