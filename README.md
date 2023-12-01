# Boilerplate app
I want to have boilerplate applications ready to build upon and deploy very quickly for whatever hare-brained idea I get, so this application will do that.

## Features
This app will have a whole MaterialUI theme, an API that can be deployed on AWS easily, and more. Really, in its finished state, it should just need to be adapted to whatever use case for whatever app I want to build in the future.

## Technical details
### Frontend local setup
React typescript bootstrapped with Create React App. I'm ripping a lot of code from [Ed Roh's React Admin Dashboard](https://github.com/ed-roh/react-admin-dashboard/) for the styling, making it work with TypeScript, and building from there.

To install and run:
```bash
cd frontend
yarn # "yarn" by itself defaults to "yarn install"
yarn start
```

### Backend local setup
Python Flask app. 

```bash
cd backend
python -m venv .
source bin/activate # this will be ".\bin\activate.bat" if on Windows
python -m pip install --no-cache-dir -r requirements.txt

cd api
python app.py
```

## Deploy setup
### Prerequisites
You must have the following to execute this full-stack deploy.

* an AWS account along with a programmatic access key configured on your computer
* AWS CLI V2 installed on your computer
* Docker Desktop installed on your computer

### Creating an ECR repository
You can execute the CFT in the root directory "ecr_repository.yaml".

```bash
aws cloudformation create-stack --stack-name ECRRepository --template-body file://ecr_repository.yaml --parameters ParameterKey=RepositoryName,ParameterValue=REPOSITORY_NAME # replace with an actual repository name
```

### Pushing your Docker images to the ECR repository
[AWS resources to push Docker images to ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)

Don't forget to start Docker Desktop before going on!

#### Docker image creation
```bash
cd backend
docker buildx build --platform linux/amd64 -t full-stack-backend  . 
cd ../frontend
docker buildx build --platform linux/amd64 -t full-stack-frontend  . 
```

#### Push to ECR
```bash
aws ecr get-login-password --region AWS_REGION --profile default | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com
docker images # verify that the new images we created are in the output, we're gonna refer to them as IMAGE_ID_FOR_BACKEND and IMAGE_ID_FOR_FRONTEND moving forward
docker tag IMAGE_ID_FOR_BACKEND AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/REPOSITORY_NAME:full-stack-backend
docker tag IMAGE_ID_FOR_FRONTEND AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/REPOSITORY_NAME:full-stack-frontend
docker push AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/REPOSITORY_NAME:full-stack-backend
docker push AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/REPOSITORY_NAME:full-stack-frontend
```

### Setting up HTTPS
You need an existing domain name. I had to create an A record pointing from a subdomain of my URL I've been using (in this case https://www.branson.solutions) called boilerplate.branson.solutions. I also had to issue a certificate in ACM covering *.branson.solutions and then update the CFT to use that certificate, since my old certificate was only valid on branson.solutions, not *.branson.solutions.

### Modifying Github Actions
There's an environment section. You will need to modify this, more later.

## Stuff I've learned from building this thing
I had minimal experience with Docker prior to building this application. I kinda wanted to do something that was not AWS Lambda flavor of serverless. I love Lambda, but I need to spread my wings and work with more flexible serverless technologies. Here is a list of important lessons I learned from putting this together, in no particular order:

* ChatGPT is a fucking godsend. I've worked with folks who swear against it with statements like "it's just a smart web crawler" or "anything it can figure I can figure out". While both of those statements are somewhat true, to that mindset I say "it's a tool to solve your problems. Use it and solve problems better and faster than before." 
* 
* Alpine Linux images with code runtime environments can be finicky for nontrivial projects. I was struggling for a while with a Node 18 Alpine Docker image in my frontend Dockerfile. It was never finishing "yarn build" even when left overnight. However, when I switched that to the Node LTS Docker image, "yarn build" finished rather quickly, and then I could still use an Alpine Nginx Docker image to actually serve the built application files.