#!/usr/bin/env ruby
sender = ARGV[0].scan(/\bfrom:.*?\]/).join
receiver = ARGV[0].scan(/\bto:.*?\]/).join
flags = ARGV[0].scan(/\bflags:.*?\]/).join
puts sender[0..-2][5..-1] + "," + receiver[0..-2][3..-1] + "," + flags[0..-2][6..-1]
