class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        Deque<Integer> dq = new ArrayDeque<>();
        for(int i=deck.length-1;i>=0;i--){
            if(!dq.isEmpty()){
                dq.addFirst(dq.pollLast());
            }
            dq.addFirst(deck[i]);
        }
        for(int i=0;i<deck.length;i++){
            deck[i] = dq.pollFirst();
        }
        return deck;
    }
}