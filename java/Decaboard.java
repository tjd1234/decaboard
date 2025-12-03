import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.AffineTransform;

public abstract class Decaboard {
    private static final String VERSION = "1.1";
    private static final int WIN_WIDTH = 500;
    private static final int WIN_HEIGHT = 500;
    private static final int CELL_SIZE = 40;
    private static final int GAP = 5;
    private static final int X_START = 30;
    private static final int Y_START = 14;
    private static final Color BG_COLOR = new Color(0, 0, 0);
    private static final Color LINE_COLOR = new Color(255, 0, 0);
    
    private static long startTime = System.currentTimeMillis();
    
    private JFrame frame;
    private DrawingPanel panel;
    
    protected Decaboard() {
        frame = new JFrame("Decaboard v" + VERSION);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        panel = new DrawingPanel();
        frame.add(panel);
        
        frame.setSize(WIN_WIDTH, WIN_HEIGHT);
        frame.setVisible(true);
    }
    
    private class DrawingPanel extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;
            
            // Enable anti-aliasing for smoother lines
            g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            
            g2d.setColor(BG_COLOR);
            g2d.fillRect(0, 0, getWidth(), getHeight());
            
            double elapsedTime = (System.currentTimeMillis() - startTime) / 1000.0;
            int x = X_START;
            int y = Y_START;
            
            for (int row = 0; row < 10; row++) {
                for (int col = 0; col < 10; col++) {
                    Double angle = angleFunction(row, col, elapsedTime);
                    if (angle == null) angle = 0.0;
                    
                    // Save the current transformation
                    AffineTransform oldTransform = g2d.getTransform();
                    
                    // Move to the center of the square
                    g2d.translate(x + CELL_SIZE/2, y + CELL_SIZE/2);
                    g2d.rotate(Math.toRadians(angle));
                    
                    // Draw the square centered at (0,0)
                    g2d.setColor(LINE_COLOR);
                    g2d.drawRect(-CELL_SIZE/2, -CELL_SIZE/2, CELL_SIZE, CELL_SIZE);
                    
                    // Restore the original transformation
                    g2d.setTransform(oldTransform);
                    
                    x += CELL_SIZE + GAP;
                }
                y += CELL_SIZE + GAP;
                x = X_START;
            }
        }
    }
    
    // Abstract method to be implemented by subclasses
    protected abstract Double angleFunction(int row, int col, double elapsedSeconds);
    
    public static void runBoard(Class<? extends Decaboard> boardClass, Integer startX, Integer startY) {
        SwingUtilities.invokeLater(() -> {
            try {
                Decaboard board = boardClass.getDeclaredConstructor().newInstance();
                if (startX != null && startY != null) {
                    board.frame.setLocation(startX, startY);
                }
                
                // Start animation
                Timer timer = new Timer(16, e -> board.panel.repaint()); // ~60 FPS
                timer.start();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public static void runBoard(Integer startX, Integer startY) {
        // Get the class that called this method
        StackTraceElement[] stackTrace = Thread.currentThread().getStackTrace();
        String callingClassName = stackTrace[2].getClassName();
        try {
            Class<?> callingClass = Class.forName(callingClassName);
            if (Decaboard.class.isAssignableFrom(callingClass)) {
                @SuppressWarnings("unchecked")
                Class<? extends Decaboard> boardClass = (Class<? extends Decaboard>) callingClass;
                runBoard(boardClass, startX, startY);
            } else {
                throw new IllegalStateException("runBoard() must be called from a subclass of Decaboard");
            }
        } catch (ClassNotFoundException e) {
            throw new IllegalStateException("Could not find calling class", e);
        }
    }
} 