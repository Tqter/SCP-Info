from urllib import request, response
import languages
import re


def filter_tags(html: str):
    # Bold and Italics
    html = html.replace("<strong>", "**").replace("</strong>", "**")
    html = html.replace("<em>", "*").replace("</em>", "*")

    # Code Blocks & quotes
    html = html.replace("&gt;", ">").replace("&lt;", "<")
    html = html.replace("&quot;", "`")

    # Random Unicode Characters
    html = html.replace("&#160;", " ")

    # Special Characters
    html = html.replace("<sup>o</sup>", "°")
    html = html.replace("<sup class>", " ")
    return html


def filter_links(html: str, language_site):
    links = html.split("<a")
    for part in range(0, len(links)):
        if links[part].find(" href=\"") != -1:
            href_data = links[part].split("\">")
            link = href_data[0].replace(" href=\"", "")
            final_link = link
            if link[0] == "/":
                final_link = f"{language_site}{link}"
            text = href_data[1].split("</a>")[0]
            full_command = f"href=\"{link}\">{text}</a>"
            links[part] = links[part].replace(
                full_command, f"[{text}]({final_link})")
    links = "".join(links)
    return links


def strike_outs(html: str):
    strikes = html.split("<span style=\"text-decoration:")
    for part in range(0, len(strikes)):
        if strikes[part].find(" line-through;\">") != -1:
            text = strikes[part].split(
                "</span>")[0].replace(" line-through;\">", "")
            full_command = f" line-through;\">{text}</span>"
            strikes[part] = strikes[part].replace(full_command, f"~~{text}~~")
    strikes = "".join(strikes)
    return strikes


def get_scp(scp_number: str, language):
    url = fr"http://www.scpwiki.com/scp-{scp_number}"

    req = request.urlopen(url)
    data = re.findall(r"<p>(.*?)</p>", req.read().decode("utf-8"))
    req.close()

    data = ("\n".join(data)).split("</iframe>")[1].split("\n")

    parsed = []
    for paragraph in range(0, len(data)):
        x = filter_links(data[paragraph], languages.langauge_to_website[language])
        x = filter_tags(x)
        x = strike_outs(x)
        parsed.append(x)
    parsed = ("\n".join(parsed)).split("&#171;")
    return "\n".join(parsed)
