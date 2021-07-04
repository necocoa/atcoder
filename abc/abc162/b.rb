n = gets.to_i
ans = 0
n.times do |i|
  if (i + 1) % 3 != 0 && (i + 1) % 5 != 0
    ans += i + 1
  end
end
puts ans