n, m = gets.split.map(&:to_i)
a_sum = gets.split.map(&:to_i).sum
if n < a_sum
  puts -1
else
  puts n - a_sum
end