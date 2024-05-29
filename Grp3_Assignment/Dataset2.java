import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

class Star {
	String name;
	int x;
	int y;
	int z;
	int weight;
	int profit;

	// Constructor to initialize the Star object
	public Star(String name, int x, int y, int z, int weight, int profit) {
		this.name = name;
		this.x = x;
		this.y = y;
		this.z = z;
		this.weight = weight;
		this.profit = profit;
	}

	// String representation of the Star object
	@Override
	public String toString() {
		return name + " " + x + " " + y + " " + z + " " + weight + " " + profit;
	}
}

public class Dataset2 {
	private static final int NUMBER_OF_STARS = 20; // Number of stars to generate
	private static final int NUMBER_OF_ROUTES = 54; // Number of routes to generate
	private static final int MIN_CONNECTIONS = 3; // Minimum number of connections for each star

	public static void main(String[] args) throws IOException {
		long seed = 3633314718L; //Sum of other group members’ ID number 
		List<Integer> digits = extractDigits(seed); // Extract digits from the seed
		Random random = new Random(seed); // Initialize Random object with the seed
		
		// List to store the generated stars
		List<Star> stars = new ArrayList<>();
		for (int i = 0; i < NUMBER_OF_STARS; i++) {
			String name = "Star " + (char) ('A' + i); // Generate star name (Star A, Star B, ...)
			int x = generateNumberUsingDigits(random, digits); // Generate random x coordinate
			int y = generateNumberUsingDigits(random, digits); // Generate random y coordinate
			int z = generateNumberUsingDigits(random, digits); // Generate random z coordinate
			int weight = generateNumberUsingDigits(random, digits, 2); // Generate random weight
			int profit = generateNumberUsingDigits(random, digits, 2); // Generate random profit
			stars.add(new Star(name, x, y, z, weight, profit)); // Add star to the list
		}

		// Initialize adjacency matrix to represent routes between stars
		int[][] adjacencyMatrix = new int[NUMBER_OF_STARS][NUMBER_OF_STARS];
		int routesCreated = 0;

		 // Randomly create the specified number of routes 
		while (routesCreated < NUMBER_OF_ROUTES) {
			int i = random.nextInt(NUMBER_OF_STARS); // Randomly select a star index
			int j = random.nextInt(NUMBER_OF_STARS); // Randomly select another star index
			if (i != j && adjacencyMatrix[i][j] == 0) {
				adjacencyMatrix[i][j] = 1; // Create route from star i to star j
				adjacencyMatrix[j][i] = 1; // Create route from star j to star i
				routesCreated++;
			}
		}

		// Ensure each star has at least the minimum number of connections
		ensureMinimumConnections(adjacencyMatrix, random);

		// Save the generated data to a file
		saveDataToFile(stars, adjacencyMatrix);
	}

	// Extract digits from the given number and return as a list
	private static List<Integer> extractDigits(long number) {
		Set<Integer> digitSet = new HashSet<>(); // Use a set to store unique digits
		while (number > 0) {
			digitSet.add((int) (number % 10)); // Extract the last digit and add to the set
			number /= 10; // Remove the last digit from the number
		}
		return new ArrayList<>(digitSet); // Convert the set to a list
	}

	// Generate a random number using the extracted digits for weight
	private static int generateNumberUsingDigits(Random random, List<Integer> digits) {
		int length = random.nextInt(3) + 1; // Random length between 1 and 3 digits
		int number = 0;
		for (int i = 0; i < length; i++) {
			number = number * 10 + digits.get(random.nextInt(digits.size())); // Add random digit to number
		}
		return number;
	}

	// Generate a random number using the extracted digits for profit
	private static int generateNumberUsingDigits(Random random, List<Integer> digits, int numDig) {
		int length = random.nextInt(numDig) + 1; // Random length between 1 and numDig digits
		int number = 0;
		for (int i = 0; i < length; i++) {
			number = number * 10 + digits.get(random.nextInt(digits.size())); // Add random digit to number
		}
		return number;
	}
	
	// Ensure each star has at least the minimum number of connections
	private static void ensureMinimumConnections(int[][] adjacencyMatrix, Random random) {
		for (int i = 0; i < adjacencyMatrix.length; i++) {
			int connections = 0;
			for (int j = 0; j < adjacencyMatrix[i].length; j++) {
				if (adjacencyMatrix[i][j] == 1) {
					connections++;
				}
			}
			// Add connections if fewer than the minimum required
			while (connections < MIN_CONNECTIONS) {
				int j = random.nextInt(adjacencyMatrix.length);
				if (i != j && adjacencyMatrix[i][j] == 0) {
					adjacencyMatrix[i][j] = 1;
					adjacencyMatrix[j][i] = 1;
					connections++;
				}
			}
		}
	}

	// Calculate the distance between two stars
	private static double calculateDistance(Star star1, Star star2) {
		return Math
				.sqrt(Math.pow(star1.x - star2.x, 2) + Math.pow(star1.y - star2.y, 2) + Math.pow(star1.z - star2.z, 2));
	}

	// Save the generated data (stars and routes) to a file
	private static void saveDataToFile(List<Star> stars, int[][] adjacencyMatrix) throws IOException {
		try (FileWriter writer = new FileWriter("Dataset2.txt")) {
			for (Star star : stars) {
				writer.write(star.toString() + "\n"); // Write each star's data to the file
			}

			writer.write("Routes:\n");
			for (int i = 0; i < adjacencyMatrix.length; i++) {
				for (int j = i + 1; j < adjacencyMatrix[i].length; j++) {
					if (adjacencyMatrix[i][j] == 1) {
						double distance = calculateDistance(stars.get(i), stars.get(j));
						writer.write(stars.get(i).name + " - " + stars.get(j).name + ": "
								+ String.format("%.2f", distance) + "\n");
					}
				}
			}
			System.out.println("Datasets generated and saved to text files.");
		}
	}
}
