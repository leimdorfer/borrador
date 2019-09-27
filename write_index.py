import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()
thisdir = thisdir+"/content"
my_content_list = []
# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if ".md" in file:
            paths = os.path.join(r, file)
            urls = paths.replace(
                "/Users/leimda01/Sites",
                "https://leimdorfer.github.io/"
            )
            urls = urls.replace(".md","")
            file = file.replace(".md","")
            my_content_list.append(" * "+"["+file+"]("+urls+")")

index_content = "My Notes"+"\n"+"============"+"\n"
index_content = index_content +"Public notes folder:"+"\n"

# Add content list
for i in my_content_list:
    index_content = index_content+i+"\n"

#"Publish" the list onto the index
f = open("index.md", "w")
f.write(index_content)
f.close()
