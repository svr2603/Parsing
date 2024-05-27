from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def get_hatnotes(browser):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    return hatnotes

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, p in enumerate(paragraphs):
        print(f"Paragraph {i+1}: {p.text[:500]}")  # print the first 500 characters
        print("\n---\n")

def list_links(browser):
    links = browser.find_elements(By.XPATH, "//a[@href]")
    link_titles = []
    for link in links:
        title = link.text
        href = link.get_attribute("href")
        if href and title:
            link_titles.append((title, href))
    for i, (title, href) in enumerate(link_titles):
        print(f"{i+1}. {title} - {href}")
    return link_titles

def main():
    browser = webdriver.Firefox()
    browser.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0')
    time.sleep(3)  # Wait for the page to load

    while True:
        print("\nChoose an option:")
        print("1. List paragraphs")
        print("2. Go to a linked page")
        print("3. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            list_paragraphs(browser)
        elif choice == '2':
            links = list_links(browser)
            link_choice = int(input(f"Choose a linked page (1-{len(links)}): "))
            if 1 <= link_choice <= len(links):
                selected_link = links[link_choice - 1][1]
                browser.get(selected_link)
                time.sleep(3)  # Wait for the page to load
            else:
                print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the program.")
            browser.quit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
