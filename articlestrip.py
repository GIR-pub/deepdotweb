### HTML Article Element Stripper
#
### Written by: DeeJayh
#
### Use for archival purposes and information retention.
### Using this program to steal information and portray it as your own,
### otherwise known as Copyright Infringement, is expressly prohibited.
### Credit people for their work. Don't be a douche.
#
### Released under the MIT License

import os, time, re

version = "1.0.2"
sTime = time.time()
filesFound = filesStripped = articles = 0

print(f"--HTML Article Element Stripper v{version}--")
print("Recursively scanning current directory and all subdirectories...")
for root, directories, filenames in os.walk(os.getcwd()):
    for file in filenames:
        title = ""
        stripped = []
        filesFound += 1
        if file == "index.html":
            print(f"Found {root}/{file}. Opening... ", end="")
            filesStripped += 1
            with open(f'{root}/{file}', encoding="utf8") as f:
                print("Done.")
                try:
                    line = f.readline()
                except Exception as e:
                    print(f"Unable to read {root}/{file}. {str(e).split(': ')[1].capitalize()}. "\
                          f"Likely a corrupt/invalid file. Skipping.")
                    print("---")
                    break
                insidearticle = False
                while line:
                    line = f.readline()
                    if line.strip().startswith("<article"):
                        stripped.append(line.strip())
                        insidearticle = True
                        articles += 1
                    elif line.strip().startswith("</article"):
                        stripped.append(line.strip() + "\n")
                        insidearticle = False
                    elif insidearticle == True:
                        if line.strip().startswith("<h1"):
                            stripped.insert(0, "---")
                            stripped.insert(0, re.split(">([^<>]+)<", line.strip())[1])
                            stripped.insert(0, "---")
                        else:
                            stripped.append("    " + line.strip())
                    else:
                        pass
                print(f"{root}/{file} stripped.")

            if len(stripped) <= 0:
                print(f"No article elements inside {root}/{file}. Skipping... ", end="")
            else:
                print(f"Writing articles to {root}/{file.split('.')[0]}.md... ", end="")
                with open(f'{root}/index.md', 'w') as f:
                    for line in stripped:
                        f.writelines(line + "\n")
            print("Done.")
            print("---")

fTime = time.time()
print("All tasks complete.")
print(f"Found {filesStripped} matching {'file' if filesStripped == 1 else 'files'} "\
      f"out of {filesFound} {'file' if filesFound == 1 else 'files'}.")
print(f"Stripped {articles} {'article' if articles == 1 else 'articles'} from "\
      f"{filesStripped} {'file' if filesStripped == 1 else 'files'}.")
print(f"Total execution time: {fTime - sTime:.2f} seconds.")
exit(0)