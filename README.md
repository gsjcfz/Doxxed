# Have I Been Doxxed Toolkit
---
# Table of Contents
1. [Overview](#overview)
    - [Introduction](#introduction)
    - [Repository Structure & Files](#repository-structure--files)
2. [App Usage](#app-usage)
    - [Running Toolkit](#running-toolkit)
    - [Requirements](#requirements) 
    - [Examples](#examples)
3. [Development](#development)
    - [Program Flow](#program-flow)
    - [Roadmap](#roadmap)
    - [To-Do](#to-do)

# Overview
With ever-expanding digital presences in the modern world, it becomes difficult to understand how much personal information is publicly available.
The **Have I Been Doxxed** toolkit seeks to provide a secure, digital footprint outline to individuals.
**Have I Been Doxxed?** plays on the idea of [Have I been pwned](https://haveibeenpwned.com/), a password leak checking tool. 

## Introduction
Brief overview of the application and its purpose.

## Repository Structure & Files
Explanation of the organization of files and folders within the repository.

# App Usage

## Running Toolkit
Instructions on how to run the application's toolkit.

## Requirements

### Installing Required Packages

To install the packages required for this application, you can use pip, a package management system for Python.

1. **Navigate to the Directory Containing requirements.txt**: Open your command-line interface (CLI) or terminal and change to the directory where the "requirements.txt" file is located.

2. **Run the pip Install Command**: Once you're in the correct directory, run the following command:

    ```
    pip install -r requirements.txt
    ```

   This command tells pip to install all the packages listed in the "requirements.txt" file.

3. **Wait for Installation to Complete**: Pip will start downloading and installing the packages one by one. Depending on the number and size of the packages, this process may take a few moments.

4. **Verify Installation**: After the installation is complete, you can verify that the packages were installed successfully by running:

    ```
    pip list
    ```

   This command will display a list of installed packages, including their versions.

5. **Optional: Virtual Environment**: It's good practice to use a virtual environment to manage dependencies for your projects. If you're not already using one, consider creating and activating a virtual environment before running the `pip install` command:

    - Create a virtual environment (in the project directory):

        ```
        python -m venv myenv
        ```

    - Activate the virtual environment:

        - On Windows:

            ```
            myenv\Scripts\activate
            ```

        - On macOS and Linux:

            ```
            source myenv/bin/activate
            ```

    With the virtual environment activated, proceed with step 2.

By following these steps, you'll have successfully installed all the required packages for the application using pip.

## Examples
Illustrative examples showcasing the usage of the application.

# Development


## Program Flow
Description of the flow of the application's functionality.

## Roadmap


## To-Do
- [ ] Integrate additional OSINT gathering tools into portfolio
  - [ ] Interactive Visualization Tool
  - [ ] Phone number analysis 
- [ ] Add report generation functionality with heuristics
  - [ ] Reliable mail client  
  - [ ] Report Generation & Artifacts/Metadata
- [ ] Beautify Initial Site
- [ ] Identification process solution
  - [ ] Possibly add a faux identification and explain in presentation that we won't pay for the API 
