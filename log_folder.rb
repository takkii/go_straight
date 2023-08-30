# frozen_string_literal: true

require 'open3'
require 'fileutils'

# Installer runner.
class InstallerRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    if Dir.exist?(File.expand_path('~/go_straight_log'))
      puts 'Already have a go_straight_log folder...do nothing.'
    else
      FileUtils.mkdir('go_straight_log')
      FileUtils.mv("#{File.dirname(__FILE__)}/go_straight_log", File.expand_path('~/'))
      puts 'Created a go_straight_log folder.'
    end
  end
end

begin
  InstallerRunner.run
rescue StandardError => e
  puts e.backtrace
ensure
  GC.compact
end

__END__
