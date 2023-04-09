class GroupSimilarTitles:
    def __init__(self):
        pass

    def generate_key(self, title):
        count = [0] * 26
        for ch in title:
            count[ord(ch) - ord('a')] += 1

        title_key = ""
        for i in range(26):
            title_key += "#" + str(count[i])

        return title_key

    def group_titles(self, titles):
        grouped_titles_map = {}

        for title in titles:
            title_key = self.generate_key(title)
            if title_key not in grouped_titles_map:
                grouped_titles_map[title_key] = []
            grouped_titles_map[title_key].append(title)

        return grouped_titles_map

if __name__ == "__main__":
    titles = ["dule", "dlue", "speed", "duel", "cars", "rasc", "depse"]
    query = "deul"

    group_similar_titles = GroupSimilarTitles()
    grouped_titles_map = group_similar_titles.group_titles(titles)
    group = grouped_titles_map[group_similar_titles.generate_key(query)]
    print(" ".join(group))
