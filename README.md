# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization process also creates a virtual environment within this project, stored under the `.venv` directory. To create the virtual environment, it assumes that there is a `python3` (or `python` for Windows) executable in your path with access to the `venv` package. If for any reason the automatic creation of the virtual environment fails, you can create it manually.

### Creating a Virtual Environment

To manually create a virtual environment on macOS and Linux:

```bash
$ python3 -m venv .venv
```

After the initialization process completes and the virtual environment is created, activate it using the following steps:

On macOS and Linux:

```bash
$ source .venv/bin/activate
```

On Windows:

```bash
% .venv\Scripts\activate.bat
```

Once the virtual environment is activated, install the required dependencies:

```bash
$ pip install -r requirements.txt
```

### Synthesizing the CloudFormation Template

After setting up the virtual environment and installing dependencies, you can synthesize the CloudFormation template:

```bash
$ cdk synth
```

To add additional dependencies, for example, other CDK libraries, just add them to your `setup.py` file and rerun the `pip install -r requirements.txt` command.

## AWS Academy Example

This project includes an example specifically designed for AWS Academy. It demonstrates a custom AWS CDK application setup using a custom bootstrap template. This template avoids creating new IAM roles and instead sets roles to `none`, so that the resources, such as the synthesizer, Lambda functions, and EC2 instances, fall back to using the `LabRole`.

To bootstrap your environment using this custom template, run:

```bash
cdk bootstrap --profile utec --template custom-bootstrap-template.yaml
```

- **`--profile utec`:** Specifies the AWS CLI profile to use. This flag is optional; if omitted, the default profile will be used.
- **`--template custom-bootstrap-template.yaml`:** Specifies the custom bootstrap template to be used instead of the default one.

### Important Notes:

- The roles for the synthesizer, Lambda functions, and EC2 instances are configured to fall back to the `LabRole`.
- This setup ensures that no new roles are created, adhering to the specific requirements of the AWS Academy example.

### Configuring AWS Academy Credentials

To use your AWS Academy credentials, ensure that you have correctly set up your AWS CLI configuration. You should place your AWS Academy credentials in the `~/.aws/credentials` and `~/.aws/config` files as follows:

In `~/.aws/credentials`:

```
[utec]
aws_access_key_id=YOUR_ACCESS_KEY_ID
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
```

In `~/.aws/config`:

```
[profile utec]
region=us-west-2
output=json
```

Replace `YOUR_ACCESS_KEY_ID` and `YOUR_SECRET_ACCESS_KEY` with your actual AWS Academy credentials.

## Useful Commands

 * `cdk ls`          - List all stacks in the app
 * `cdk synth`       - Emit the synthesized CloudFormation template
 * `cdk deploy`      - Deploy this stack to your default AWS account/region
 * `cdk diff`        - Compare deployed stack with current state
 * `cdk docs`        - Open CDK documentation
