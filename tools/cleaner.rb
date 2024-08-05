# frozen_string_literal: true

require 'fileutils'
require 'open3'
require 'readline'

# Create runner.
class CleanRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.delete
    puts ''
    puts 'Enter yes/no to delete, tab completion is available.'
    puts ''

    sel = %w[yes no].map!(&:freeze).freeze

    Readline.completion_proc = proc {|word|
      sel.grep(/\A#{Regexp.quote word}/)
    }

    while (line = Readline.readline(""))
      line.chomp!

      if line.match?(sel[0])
        FileUtils.rm_rf(File.expand_path('~/go_straight_log'))
        puts ''
        puts 'Deleted, the existing go_straight_log folder.'
        puts ''
        break
      elsif line.match?(sel[1])
        puts ''
        puts 'You selected No, No action will be taken.'
        puts ''
        break
      else
        puts ''
        puts 'Please enter yes or no as an argument.'
        puts ''
        break
      end
    end
  end

  def self.run
    encoding_style
    if Dir.exist?(File.expand_path('~/go_straight_log'))
      puts ''
      puts 'Already have a go_straight_log folder.'
      delete
    else
      FileUtils.mkdir('go_straight_log')
      FileUtils.mv("#{File.dirname(__FILE__)}/go_straight_log", File.expand_path('~/'))
      puts ''
      puts 'Created, go_straight_log folder.'
      puts ''  
    end
  end
end

begin
  CleanRunner.run
rescue StandardError => e
  puts e.backtrace
ensure
  GC.compact
end

__END__
