public class Example extends Decaboard {
    @Override
    protected Double angleFunction(int row, int col, double elapsedSeconds) {
        return 5.0 * Math.max(row, col) * elapsedSeconds;
        // return 47.5;
    }

    public static void main(String[] args) {
        // Start the board at position (1200, 200) on the screen
        runBoard(1200, 200);
    }
} 