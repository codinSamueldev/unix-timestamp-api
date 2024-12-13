# Unix To Date Format API
[![SJaMj.png](https://s7.gifyu.com/images/SJaMj.png)](https://gifyu.com/image/SJaMj)

This API convert date format _(YY-MM-DD)_ to unix seconds code and vice-versa. It was built in FastAPI.

> [!IMPORTANT]
> The API could take up to 1 minute loading due to the free host service (Hope you understand 🙈)

## Why FastAPI?
The project is proposed by FreeCodeCamp in the backend [lectures](https://www.freecodecamp.org/learn/back-end-development-and-apis/#back-end-development-and-apis-projects) as the first of five projects to complete so as to get the Backend certification.
They teach this learning route with JS, so obviously these projects should be completed in that language. Nevertheless, I chose not to make excuses and made up my mind to complete this first one.
Then, I remembered that I have built a few side API's projects with FastAPI, so decided to refresh a bit my FastAPI skills and give it a try.

## How it works?
It is pretty simple. Go to the url and write after the .com the following: 

    /api/2024-12-24              
Then hit enter, and that's it!       
Of course, I you would like to change the date
feel free to do it,  ***just remember*** to keep the format _(YY-MM-DD)_

## What did I learn?
I have strengthen my knowledge on the datetime module that offers Python, which built-in datetime methods can help us to turn datetime objects into unix code.   
I have learned that FastAPI can work with templates (thanks to Jinja2Templates), which for a Django developer myself, it is quite essential working with templates.
Get to know more Pytest and how easy is to parametrize tests with this testing framework. 
