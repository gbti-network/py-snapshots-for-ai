Hello there! 

I have a new version of my project "Hello World tutorial for NextJS" that I'd like you to review. 
This markdown document shows my updated file structure as well as the content of my file changes. 
Please review and report back your understanding of the project. Thanks! 

# Project Structure

+ pages/
    - about.js
    + day/
        - index.js
    - index.js
- README.md
- render.yaml


# Project Files

## .\pages\about.js
```
const About = () => <div>About us</div>;
export default About;

```

## .\pages\day\index.js
```
const Day = () => <div>Hello Day</div>;
export default Day;

```

## .\pages\index.js
```
import Link from 'next/link'
const Index = () => (
  <div>
    Hello World.{' '}
    <Link href="/about">
      <a>About</a>
    </Link>
  </div>
)
export default Index;

```

## .\README.md
```
# Next.js Hello World

This repo is forked from [nextjs/examples/hello-world](https://github.com/zeit/next.js/tree/canary/examples/hello-world).

This example shows the most basic idea behind Next. We have 2 pages: `pages/index.js` and `pages/about.js`. The former responds to `/` requests and the latter to `/about`. Using `next/link` you can add hyperlinks between them with universal routing capabilities. The `day` directory shows that you can have subdirectories.

The app in this repo is deployed at https://next-js.onrender.com.

## Deploy

Click the button below to deploy this app on Render.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

```

## .\render.yaml
```
services:
- type: web
  name: next-js
  env: node
  plan: starter
  buildCommand: yarn; yarn build
  startCommand: yarn start
  autoDeploy: false
  envVars:
  - key: NODE_ENV
    value: production
# Uncomment the following to deploy this app as a static site on render
# - type: web
#   name: nextjs-static
#   env: static
#   buildCommand: yarn; yarn build; yarn next export
#   staticPublishPath: out
#   pullRequestPreviewsEnabled: true     # optional
#   envVars:
#   - key: NODE_ENV
#     value: production


```

