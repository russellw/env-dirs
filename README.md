Find directories from environment variables.

That is, look through all currently set environment variables, check which ones specify one or more directories, and print them in a readably formatted list.

Optionally, take a list of filenames (which can include wildcards) and only print the directories that contain a file matching something from the list. The intent is to answer questions like 'there are 19 versions of System.Numerics.dll scattered around my machine; how is the C# compiler figuring out where to find the one it finds, and which one is that?' (the actual example that motivated writing the script).

Currently Windows-specific. Pull requests for Unix adaptation welcome!
