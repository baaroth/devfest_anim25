package devfest;

import java.util.List;

public record RandomlyFilled<T extends Comparable<T>>(List<T> values, Class<T> type) {
	public RandomlyFilled(List<T> values, Class<T> type) {
		this.values = List.copyOf(values);
		this.type = type;
	}

	public int size() {
		return values.size();
	}
}
