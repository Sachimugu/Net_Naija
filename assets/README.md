# SageMaker Hands-On on AWS

![ViewCount](https://views.whatilearened.today/views/github/debdattasarkar/SageMaker-Practice-on-AWS.svg?cache=remove)
![GitHub top language](https://img.shields.io/github/languages/top/debdattasarkar/SageMaker-Practice-on-AWS?style=flat)
![GitHub language count](https://img.shields.io/github/languages/count/debdattasarkar/SageMaker-Practice-on-AWS?style=flat)
![Stars Badge](https://img.shields.io/github/stars/debdattasarkar/SageMaker-Practice-on-AWS?style=flat)
![Forks Badge](https://img.shields.io/github/forks/debdattasarkar/SageMaker-Practice-on-AWS?style=flat)
![Pull Requests Badge](https://img.shields.io/github/issues-pr/debdattasarkar/SageMaker-Practice-on-AWS?style=flat)
[![Total Downloads](https://img.shields.io/github/downloads/debdattasarkar/SageMaker-Practice-on-AWS/total.svg)](https://github.com/debdattasarkar/SageMaker-Practice-on-AWS/releases/)

### 💻  Practical Appilcation of Real Life Scenarios on AWS SageMaker Studio / Notebook Instances

| <b>Name</b> | <b>Source</b> |
| :--- | :---: |
| <a href="https://github.com/debdattasarkar/SageMaker-Practice-on-AWS/blob/master/1%20Employee%20Salary%20Prediction%20-%20Using%20AWS%20SageMaker%20Linear%20Learner/employee_salary_prediction_notebook.ipynb"><em>Employee Salary Prediction - Using AWS SageMaker Linear Learner</em></a> | [![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=flat-square&logo=Udemy&logoColor=white)](https://www.udemy.com/course/practical-aws-sagemaker-6-real-world-case-studies/) |
| <a href="https://github.com/debdattasarkar/SageMaker-Practice-on-AWS/blob/master/2%20Medical%20Insurance%20Premium%20Prediction%20-%20Linear%20Learner%20-%20Artificial%20Neural%20Network/medical_insurance_prediction_notebook.ipynb"><em>Medical Insurance Premium Prediction - Linear Learner - Artificial Neural Network</em></a> | [![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=flat-square&logo=Udemy&logoColor=white)](https://www.udemy.com/course/practical-aws-sagemaker-6-real-world-case-studies/) |
| <a href="https://github.com/debdattasarkar/SageMaker-Practice-on-AWS/blob/master/3%20Retail%20Sales%20Prediction%20-%20Using%20AWS%20SageMaker%20XGBoost%20(Regression)/retail_sales_forecast_notebook.ipynb"><em>Retail Sales Prediction - Using AWS SageMaker XGBoost (Regression)</em></a> | [![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=flat-square&logo=Udemy&logoColor=white)](https://www.udemy.com/course/practical-aws-sagemaker-6-real-world-case-studies/) |

### 🤺 AWS Sagemaker CLI Commands

<details>
<summary>1. Retrieve the list of domains in your account.</summary>

```
aws --region Region sagemaker list-domains
```
Example
```
aws --region us-east-2 sagemaker list-domains
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker list-domains
{
    "Domains": [
        {
            "DomainArn": "arn:aws:sagemaker:us-east-2:807100423897:domain/d-mxkxcy82frnd",
            "DomainId": "d-mxkxcy82frnd",
            "DomainName": "default-1634999453430",
            "Status": "InService",
            "CreationTime": "2021-10-23T14:30:55.857000+00:00",
            "LastModifiedTime": "2021-10-23T14:35:41.514000+00:00",
            "Url": "https://d-mxkxcy82frnd.studio.us-east-2.sagemaker.aws"
        }
    ]
}
```
</details>

<details>
<summary>2. Retrieve the list of applications for the domain to be deleted.</summary>

```
aws --region Region sagemaker list-apps \
    --domain-id-equals DomainId
```
Example
```
aws --region us-east-2 sagemaker list-apps \
        --domain-id-equals d-mxkxcy82frnd
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker list-apps \
>         --domain-id-equals d-mxkxcy82frnd
{
    "Apps": [
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "AppType": "KernelGateway",
            "AppName": "datascience-1-0-ml-t3-medium-b3043d3e6163713f99726df4a911",
            "Status": "InService",
            "CreationTime": "2021-10-23T14:40:45.328000+00:00"
        },
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "AppType": "JupyterServer",
            "AppName": "default",
            "Status": "InService",
            "CreationTime": "2021-10-23T14:36:16.825000+00:00"
        }
    ]
}
```
</details>

<details>
<summary>3. Delete each application in the list.</summary>

```
aws --region Region sagemaker delete-app \
    --domain-id DomainId \
    --app-name AppName \
    --app-type AppType \
    --user-profile-name UserProfileName
```
Example
```
aws --region us-east-2 sagemaker delete-app \
    --domain-id d-mxkxcy82frnd \
    --app-name default \
    --app-type JupyterServer \
    --user-profile-name debdattasagemaker
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker delete-app \
>     --domain-id d-mxkxcy82frnd \
>     --app-name default \
>     --app-type JupyterServer \
>     --user-profile-name debdattasagemaker

[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker list-apps \
>         --domain-id-equals d-mxkxcy82frnd
{
    "Apps": [
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "AppType": "KernelGateway",
            "AppName": "datascience-1-0-ml-t3-medium-b3043d3e6163713f99726df4a911",
            "Status": "InService",
            "CreationTime": "2021-10-23T14:40:45.328000+00:00"
        },
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "AppType": "JupyterServer",
            "AppName": "default",
            "Status": "Deleted",
            "CreationTime": "2021-10-23T14:36:16.825000+00:00"
        }
    ]
}
```

```
aws --region us-east-2 sagemaker delete-app \
    --domain-id d-mxkxcy82frnd \
    --app-name datascience-1-0-ml-t3-medium-b3043d3e6163713f99726df4a911 \
    --app-type KernelGateway \
    --user-profile-name debdattasagemaker
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker list-apps         --domain-id-equals d-mxkxcy82frnd{
    "Apps": [
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "AppType": "KernelGateway",
            "AppName": "datascience-1-0-ml-t3-medium-b3043d3e6163713f99726df4a911",
            "Status": "Deleted",
            "CreationTime": "2021-10-23T14:40:45.328000+00:00"
        },
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "AppType": "JupyterServer",
            "AppName": "default",
            "Status": "Deleted",
            "CreationTime": "2021-10-23T14:36:16.825000+00:00"
        }
    ]
}
```
</details>

<details>
<summary>4. Retrieve the list of user profiles in the domain.</summary>

```
aws --region Region sagemaker list-user-profiles \
    --domain-id-equals DomainId
```
Example
```
aws --region us-east-2 sagemaker list-user-profiles \
    --domain-id-equals d-mxkxcy82frnd
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker list-user-profiles \
>     --domain-id-equals d-mxkxcy82frnd
{
    "UserProfiles": [
        {
            "DomainId": "d-mxkxcy82frnd",
            "UserProfileName": "debdattasagemaker",
            "Status": "InService",
            "CreationTime": "2021-10-23T14:35:46.247000+00:00",
            "LastModifiedTime": "2021-10-23T14:35:50.802000+00:00"
        }
    ]
}
```
</details>

<details>
<summary>5. Delete each user profile in the list. </summary>

```
aws --region Region sagemaker delete-user-profile \
    --domain-id DomainId \
    --user-profile-name UserProfileName
```
Example
```
aws --region us-east-2 sagemaker delete-user-profile \
    --domain-id d-mxkxcy82frnd \
    --user-profile-name 
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker delete-user-profile \
>    --domain-id d-mxkxcy82frnd \
>    --user-profile-name debdattasagemaker
```
</details>

<details>
<summary>6. Delete the domain. To also delete the Amazon EFS volume, specify HomeEfsFileSystem=Delete. </summary>

```
aws --region Region sagemaker delete-domain \
    --domain-id DomainId \
    --retention-policy HomeEfsFileSystem=Retain
```
Example
```
aws --region us-east-2 sagemaker delete-domain \
    --domain-id d-mxkxcy82frnd \
    --retention-policy HomeEfsFileSystem=Delete
```
Output
```
[cloudshell-user@ip-10-0-137-51 ~]$ aws --region us-east-2 sagemaker delete-domain \
>     --domain-id d-mxkxcy82frnd \
>     --retention-policy HomeEfsFileSystem=Delete
```
</details>

### ⛏️ Skills Applied

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)



#### © Copyright 2021 - [Debdatta Sarkar](https://github.com/debdattasarkar)
<a href="https://www.linkedin.com/in/debdatta-sarkar/"> ![LinkedIn Profile](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) </a>
