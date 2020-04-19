n = gets.to_i
a = gets.split.map(&:to_i)

ans = [0] * n
a.each { |b| ans[b - 1] += 1 }

puts ans