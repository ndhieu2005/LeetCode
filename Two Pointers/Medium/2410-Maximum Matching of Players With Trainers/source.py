class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort() #1,2,3,....
        trainers.sort() #1,2,3,...
        count = 0
        while players and trainers:
            if players[0] <= trainers[0]:
                heapq.heappop(players)
                heapq.heappop(trainers)
                count += 1
            else:
                heapq.heappop(trainers)
        return count


        