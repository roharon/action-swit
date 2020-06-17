# Swit for Github Action

![Publish Docker Image](https://github.com/roharon/action-swit/workflows/Publish%20Docker%20Image/badge.svg)
[![GitHub Releases](https://img.shields.io/github/release/roharon/action-swit.svg)](https://github.com/roharon/action-swit/releases)

Send a message to Swit using Github Actions

## Inputs

### `webhooks_url`

**Required** Your App's webhooks_url


### `message`

**Required** The message send to swit. Default 
`"Build Success. ${{ github.sha }}"`



## Example Usage

```yml
uses: actions/action-swit@v1
with:
  webhooks_url: 'https://hook.swit.io/chat/~~~/~~~'
  message: 'Build Success ${{ github.sha }}
```

## How to get my webhooks_url?

First, [Create your swit app](https://developers.swit.io/apps)

Second, Enable Webhook URL & Click Add New Webhook

*Choose channel or project you want 🙃*
![image](https://user-images.githubusercontent.com/4939738/84921445-72f48d00-b0ff-11ea-9d59-e8b5169e7d74.png)
