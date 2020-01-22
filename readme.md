## Python Project for AWS Lambda

This is python skeleton project for AWS Lambda, integrate with API Gateway using Proxy.
This project support debug locally with mock request in debug.py

#### Project Structure
- Config 
    - Here all your config file belong
- Controller
    - Control your api path to specific service
- Decorator
    - Here all your decorator file belong
- Exception
    - Here specify exception for any request
- Service
    - Here logic for each function placed
- Util
    - Here util belong for this project    
- Vo
    - Here request/response model belong

#### Requirement
- Python 3.xx

#### How to debug?
Just type and enter `python debug.py` on your terminal

#### Add library
If you need add dependency library, just execute this `pip install <package_name> --target vendor/`
```
Maintainer : Reza Andriyunanto

andriyunantoreza@gmail.com
```