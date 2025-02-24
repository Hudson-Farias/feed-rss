from feedgen.feed import FeedGenerator


def feed_generator(title: str, description: str) -> FeedGenerator:
    fg = FeedGenerator()
    fg.id('https://example.com/rss')
    fg.title(title)
    fg.link(href = 'https://example.com', rel = 'alternate')
    fg.language('pt-br')
    fg.description(description)

    return fg
