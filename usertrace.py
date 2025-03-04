import requests
import argparse
from colorama import Fore, Style;
import time;

SITES = {
    # Social Media
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "Threads": "https://www.threads.net/@{}",
    "VK": "https://vk.com/{}",

    # Developer & Tech
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "Replit": "https://replit.com/@{}",
    "CodePen": "https://codepen.io/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Dev.to": "https://dev.to/{}",
    "Hashnode": "https://hashnode.com/@{}",

    # Gaming
    "Steam": "https://steamcommunity.com/id/{}",
    "Xbox Live": "https://www.xboxgamertag.com/search/{}",
    "PlayStation Network": "https://psnprofiles.com/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "Epic Games": "https://www.epicgames.com/id/{}",
    "Minecraft": "https://namemc.com/profile/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Discord": "https://discord.com/users/{}",
    "Speedrun.com": "https://www.speedrun.com/user/{}",
    "Osu!": "https://osu.ppy.sh/users/{}",
    "Chess.com": "https://www.chess.com/member/{}",
    "Lichess": "https://lichess.org/@/{}",
    
    # Marketplaces
    "Amazon": "https://www.amazon.com/profile/{}",
    "Etsy": "https://www.etsy.com/people/{}",
    "eBay": "https://www.ebay.com/usr/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Upwork": "https://www.upwork.com/freelancers/~{}",
    "Alibaba": "https://www.alibaba.com/profile/{}",
    "AliExpress": "https://www.aliexpress.com/store/{}",

    # Music & Streaming
    "Spotify": "https://open.spotify.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "Audiomack": "https://audiomack.com/{}",

    # Blogging & Writing
    "Medium": "https://medium.com/@{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Substack": "https://{}.substack.com",
    "WordPress": "https://{}.wordpress.com",
    "Tumblr": "https://{}.tumblr.com",
    "Blogger": "https://{}.blogspot.com",
    "LiveJournal": "https://{}.livejournal.com",

    # Design & Art
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "ArtStation": "https://www.artstation.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "CGSociety": "https://{}.cgsociety.org",
    
    # Cryptocurrency
    "OpenSea": "https://opensea.io/{}",
    "Rarible": "https://rarible.com/{}",
    "Foundation": "https://foundation.app/@{}",
    "Binance": "https://www.binance.com/en/user/{}",
    "CoinGecko": "https://www.coingecko.com/en/people/{}",
    "Crypto.com": "https://crypto.com/nft/profile/{}",

    # Forums & Communities
    "4chan": "https://boards.4chan.org/u/{}",
    "8kun": "https://8kun.top/{}",
    "Something Awful": "https://forums.somethingawful.com/member.php?action=getinfo&username={}",
    "ResetEra": "https://www.resetera.com/members/{}",
    "NeoGAF": "https://www.neogaf.com/members/{}",
    "Gaia Online": "https://www.gaiaonline.com/profiles/{}/",

    # Academic & Science
    "Google Scholar": "https://scholar.google.com/citations?user={}",
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "Academia.edu": "https://{}.academia.edu",
    "ORCID": "https://orcid.org/{}",
    "ArXiv": "https://arxiv.org/search/?query={}",

    # Others
    "Wayback Machine": "https://web.archive.org/web/*/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Gist": "https://gist.github.com/{}",
    "Keybase": "https://keybase.io/{}",
    "LibraryThing": "https://www.librarything.com/profile/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "FanFiction": "https://www.fanfiction.net/u/{}",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}

def user_exists(username):
  urls = [];
  for site, url in SITES.items():
    full_url = url.format(username)
    try:
      response = requests.get(full_url, headers=HEADERS, timeout=5)
      if response.status_code == 200:
        urls.append(full_url);
        print(f"{Fore.GREEN}[{site}] {username} exists! (OK){Style.RESET_ALL}")
      else:
        print(f"{Fore.RED}[{site}] {username} does not exist! (ERR){Style.RESET_ALL}")
    except requests.RequestException:
      print(f"{Fore.YELLOW}[{site}] {username} Error: Unable to check (TIMEOUT/ERROR){Style.RESET_ALL}")
    
  return urls;
  
def main():
  parser = argparse.ArgumentParser(description="Simplest Username Checker")
  parser.add_argument("usernames", nargs="+", help="Username(s) to check")
  parser.add_argument("-o", "--output", help="Save urls to a file")

  args = parser.parse_args()
  time_started = time.time();
  results = [];
  
  for username in args.usernames:
    results.append(user_exists(username));
  
  print(f"took {(time.time() - time_started) / 60} minutes to complete");
  
  if args.output:
    with open(args.output, "w") as f:
      for result in results:
        f.write("\n".join(result))
      print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main()