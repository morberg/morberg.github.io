# %%
import glob


# %%
def prepend_redirect_frontmatter(filename: str):
    """Add redirect frontmatter to file"""

    frontmatter = f"""---
layout: redirected
sitemap: false
permalink: /{filename}
redirect_to: /recept/{filename}
---

"""

    with open(filename, "r") as f:
        original = f.read()

    with open(filename, "w") as f:
        f.write(frontmatter + original)


# %%
all_html_files = glob.glob("**/*.html", recursive=True)
do_not_modify = ["index.html", "README.html", "_layouts/redirected.html"]
files_to_modify = [line for line in all_html_files if line not in do_not_modify]

for filename in files_to_modify:
    print(f"Adding frontmatter to {filename}")
    prepend_redirect_frontmatter(filename)

# %%
