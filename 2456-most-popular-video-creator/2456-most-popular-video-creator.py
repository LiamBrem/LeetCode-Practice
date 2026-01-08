class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        answer = []

        # creator: PQ of videos
        videos = defaultdict(list)
        popularity = defaultdict(int)

        for i in range(len(creators)):
            creator, ide, view = creators[i], ids[i], views[i]
            popularity[creator] += view
            heapq.heappush(videos[creator], (-view, ide))

        popularitySorted = sorted(popularity.items(), key=lambda item: item[1])

        highest = popularitySorted[-1][1]
        while popularitySorted and popularitySorted[-1][1] == highest:
            person = popularitySorted[-1][0]
            res = [person]
            video = heapq.heappop(videos[person])
            res.append(video[1])
            answer.append(res)
            popularitySorted.pop()

        return answer