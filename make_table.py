### deifne some stuff
heading = f"""
<html>
<head/><link rel="stylesheet" href="default.css">
<head>
    <title>Adam Caulfield</title>
    <!-- <meta http-equiv="Refresh" content="0; url='https://adamicaulfield.github.io/'" /> -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"/>
    <meta http-equiv="Pragma" content="no-cache"/>
    <meta http-equiv="Expires" content="0"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&family=Roboto:wght@300&display=swap" rel="stylesheet">
</head>

<body>

<div class="banner">
    <div class="top-banner">
    <nav>
      <ul style="margin-top:0pt">
        <li><a href="./index.html">Home</a></li>
        <li><a href="./research.html">Research</a></li>
        <li><a href="./experiences.html">Experiences</a></li>
        <li><a href="./links.html">My Links</a></li>
      </ul>
    </nav>
    </div>
</div>

<div class="main-content">
<h3>Conference Deadlines</h3>
"""

footer = f"""
</div>
</body>
</html>
"""

csv_file = open("test.csv", 'r')
csv_data = csv_file.readlines()
csv_file.close()

print(type(csv_data))
print(type(csv_data[0]))


### lets do it
html_file = open("./deadlines.html", "w")

print(heading, file=html_file)
print("<table>", file=html_file)
first = True
for i in range(0, len(csv_data)-1):
    line = csv_data[i]
    line = line.replace("\n",'')
    row_elts = line.split(',')

    # print(line)
    if first:
        print("\t<thead>", file=html_file)
        
    print("\t\t<tr>", file=html_file)
    for elt in row_elts:
        if elt == row_elts[-1] and not first:
            print(f"\t\t\t<td><a href=\"{elt}\">Link</a></td>", file=html_file)
        elif first:
            print(f"\t\t\t<td><span style=\"font-weight:bold\">{elt}</span></td>", file=html_file)
        else:
            print(f"\t\t\t<td>{elt}</td>", file=html_file)
    print("\t\t</tr>", file=html_file)

    if first:
        print("\t</thead>", file=html_file)
        print("\t<tbody>", file=html_file)
        first = False

    # print(row_elts)
print("\t</tbody>", file=html_file)
print("</table>", file=html_file)
print(footer, file=html_file)