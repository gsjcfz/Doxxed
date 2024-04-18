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
1. **Download Microsoft Visual Studio Community**: https://visualstudio.microsoft.com/downloads/
2. Run the installer, and make sure to select Asp.Net web development when you are given the option. If you forget to do this, you can always re-run the installer and modify from the Workloads tab.

1. **Download Microsoft SQL Express**: https://www.microsoft.com/en-us/download/details.aspx?id=101064
2. Run the installer, I did the basic installation.
3. After the installation is complete, note your connection string: **Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;**
4. You can also install SQL Server Management studio (SSMS) which will give you a better look at the database schema, but this isn't required.

1. **Clone the GitHub files from your github repo into the file directory where you want your project.**
2. I used command prompt, but you could also do it directly in visual studio.

1. **Open the Doxxed.sln file with Visual Studio to open the project**
2. Run the debugger by pressing the green triangle button that says "https". Note: if you get an error about the target SDK being .Net 8.0, you need to upgrade your Visual Studio to the latest version.
3. You will likely be asked to install two certificates, accept and install both of them
4. Your default browser should launch. You may have to allow unsafe sites to access the page (chrome://flags/#allow-insecure-localhost to allow only for localhost)

1. **To migrate the database for login system functionality**
2. open tools-> NuGet Package Manager -> Console
3. Type 'Add-Migration "Database""'
4. After the build succeeds, type "Update-Database". This should insert all the neccessary tables into your sqlserver.

**You can now register an account and login to the tool.**


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
- [ ] Tripp: Integrate additional OSINT gathering tools into portfolio
  - [ ] Interactive Visualization Tool
  - [ ] Phone number analysis
  - [ ] Look for new OSINT gathering tools 
- [ ] Add report generation functionality with heuristics
  - [ ] Avery: Reliable mail client written in Python. Be able to send a random pdf to a specified email address.
  - [ ] Nick & Tripp: Report Generation & Artifacts/Metadata, create PDF from updated OSINT info
- [ ] Alex: Identification process solution
  - [ ] Possibly add a faux identification and explain in presentation that we won't pay for the API
- [ ] Grant: Add instructions for how to run program after first install
- [ ] Grant: Alter our html for PDF display
