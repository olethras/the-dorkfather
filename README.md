<p align='center'>
    <img src='https://files.catbox.moe/8ja2yi.png' height='167px' width='227px'>
</p>

<div align='center'>
	<h4><i>The Dorkfather is a module based google dork generator using custom keywords.</i><br></h4>
</div>

<p align='center'>
    <img src='https://files.catbox.moe/p3khxs.png' height='239px' width='537px'>
</p>

# Preface

Finding data resources can become a time consuming task that's why, most of the time, I end up using Google Dorks to limit my search results and make them more 'targeted' to what I am actually trying to find.

This totally makes the job easier, but yet again even simple Google Dorks might not be enough to find what I am looking for - so I end up crafting even more detailed dorks, thus losing more time doing research rather than actually acquiring data. 

To encounter this I created a tool that can help me craft multiple detailed google dorks really fast based on keywords and modules that aim to return the results that I'm truly looking for, The Dorkfather.

# Documentation

The Dorkfather uses modules, you can think of modules as 'what you are actually looking for' - for example, if I am looking for datasets containing information (Spreadsheets, databases, csv files, etc.), I'm going to use the 'dataset' module.

Modules are great because you don't have to 'explain' what you are looking for using the keywords, you just specify the module you want to use in your dorks and The Dorkfather takes care of everything.

Keywords are used to specify 'what type of information you want your results to contain' - for datasets containing 'passwords' information, the command in The Dorkfather would look like this:

```bash
python dorkfather.py 1 passwords
```

As you can see, I parsed 2 arguments to the CLI. '1' is the module number for the 'dataset' module and 'passwords' is my custom keyword. This shall generate dorks I can query to google to fetch the results I want.

You can parse multiple keywords to the CLI - for example:

```bash
python dorkfather.py 1 passwords,accounts,emails,usernames,..
```

The Dorkfather will generate dorks with all the possible combinations of your keywords, another thing you don't have to worry about.

## Things to consider

1. Please make sure you are running The Dorkfather using python 3.10!
2. Make any suggestions regarding new modules you'd be interested in.














