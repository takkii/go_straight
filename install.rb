# frozen_string_literal: true
#!/usr/bin/ruby

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
    if Dir.exist?(File.expand_path('~/config'))
      stdout_rb, _stderr_rb, _status_rb = Open3.capture3("ruby ./uninstall.rb")
      stdout_rb
      stdout_gt, _stderr_gt, _status_gt = Open3.capture3("git clone git@github.com:takkii/config.git")
      stdout_gt
      FileUtils.mv("#{File.dirname(__FILE__)}/config", File.expand_path('~/'))
    else
      stdout_gt, _stderr_gt, _status_gt = Open3.capture3("git clone git@github.com:takkii/config.git")
      stdout_gt
      FileUtils.mv("#{File.dirname(__FILE__)}/config", File.expand_path('~/'))
    end
  end
end

InstallerRunner.run
