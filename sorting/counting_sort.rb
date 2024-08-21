#!/usr/bin/env ruby

# counting sort
#
# Great for sorting integers within a known range of k, especially
# when there are lots of duplicates.
#
# Runtime O(n + k), memory O(k)


def sort(list)
  min = list.min
  max = list.max

  counts = [0] * (max - min + 1)
  list.each { |x| counts[x - min] += 1 }

  res = []
  counts.each.with_index(min) do |count, i|
    count.times { res << i }
  end

  res
end


if __FILE__ == $0
  data = [ 1, 1, 2, 2, 3 ].shuffle
  puts data.join(' ')
  puts sort(data).join(' ')
end


################  RSpec  ################

require 'rspec'

describe 'sort' do
  it 'sorts positive ints' do
    100.times do |i|
      data = (rand(i + 1) + 1).times.map { rand(100) }

      expect(sort(data)).to eq(data.sort)
    end
  end

  it 'sorts all ints' do
    100.times do |i|
      data = (rand(i + 1) + 1).times.map { rand(-100..100) }

      expect(sort(data)).to eq(data.sort)
    end
  end
end
