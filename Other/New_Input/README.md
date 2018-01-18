From email-

Hi Shelley,

I think mocking the input function with a different approach to the legacy code we have might be a better solution to the problem. This way you can just use the PythonTestCase and don't have to worry about the old StudentTestCase for which you don't know the implementation of some functions. I am attaching a zip with the test and attempt, that takes an absolute value problem that receives an input at the beginning, and then patches the input function during testing.  It then does the same to stdout to check for assertions. 

It should be noted that if you want to run code that is not inside a function and is just a script, you need to have the setUp function provided so that it deletes the python cache and reruns the module after every test. Otherwise, if your code is inside a function you can just execute it after the import ( attempt.functionName() in this case) . 

Just tried this with the PythonTestCase in mypy and it works so I hope this will be useful. As always let us know if anything else comes up.

Cheers,

Diego 
