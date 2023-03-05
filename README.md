# perplexity-thing
this is an api wrapper of perplexity.ai that was made by me, a very dumb fella.
(i am new to github and python in general, so please don't expect me to fix all of the bugs :>)


**Usage:**

you can use the python file in your project by importing it:

```import perplexitymain```

due to the fact that i don't know how to make good wrappers, this script uses selenium and Chrome to get the text and other stuff. to download it, go to https://chromedriver.chromium.org/downloads

to send a request, you need to call ```ask(*your input text*, *path to chrome*)```

you will get a list of multiple objects, the first is going to be the main text that the ai has generated, and the others are the sources.

Please expect for this script not to work sometimes <3


**TODO:**

* Add a proper way to send requests to the webstite
* (somehow) bypass the cloudflare  check
* add a support for a follow up


*also please dont sue me this is a small test project, i will take it down if this gets illegal :[*
