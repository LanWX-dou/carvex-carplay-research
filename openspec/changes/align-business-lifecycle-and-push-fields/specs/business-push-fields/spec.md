## ADDED Requirements

### Requirement: Field publication has traceable authority and evidence

The sender SHALL publish fields only under the actual message-direction capabilities, subscription/component selection and traceable source contract. Its field matrix SHALL distinguish confirmed protocol facts, local policy and unresolved source/units. A user-requested trial MUST remain labeled as a trial until supported by evidence.

#### Scenario: Total distance is still a trial
- **WHEN** the existing user-requested total_distance-to-p7 trial is tested
- **THEN** its source marker and unresolved role SHALL be retained
- **AND** the implementation SHALL NOT manufacture remaining time or ETA from that value

#### Scenario: A lane source is absent
- **WHEN** no verified lane provider or required lane/display capability is available
- **THEN** the sender SHALL NOT publish fabricated 5204 data
- **AND** the corresponding implementation task SHALL remain incomplete

### Requirement: NowPlaying updates preserve explicit field meaning

NowPlaying publication SHALL respect the valid 5000 selection and the proven initial-update contract. It SHALL distinguish omitted fields from explicit clears and zero values. Replacing a media item MUST handle previously retained selected fields using a documented clear contract without treating unknown live values as observed zero values.

#### Scenario: Only progress changes
- **WHEN** an incremental 5001 update contains elapsed time but omits title and artist
- **THEN** receivers SHALL retain the valid title and artist for that media item

#### Scenario: A new track lacks the previous artist
- **WHEN** a media item is replaced and its artist is unavailable
- **THEN** the publisher SHALL follow the verified clear/unknown contract instead of silently carrying the previous track's artist
- **AND** its tests SHALL verify the retained receiver state

### Requirement: Artwork and player commands retain separate completion semantics

Artwork SHALL use the established file-transfer channel and reference rather than embedding image bytes in 5001. A 5003 request SHALL distinguish parsing, platform request delivery and observed execution; unimplemented player operations MUST NOT be reported as executed through a local snapshot rewrite.

#### Scenario: Old artwork finishes late
- **WHEN** a transfer for a previous media item or owner completes after replacement
- **THEN** it SHALL NOT overwrite the current item's artwork

#### Scenario: A player request lacks an execution provider
- **WHEN** a valid 5003 player operation cannot be delivered to a real provider
- **THEN** the missing execution path SHALL remain explicit
- **AND** changing a cached elapsed/index value alone SHALL NOT count as successful execution

### Requirement: Navigation definitions and references stay within negotiated capacity

Navigation publication SHALL derive components and options from valid START and display limits from Identification. Each maneuver definition/reference batch SHALL remain consistent across the current snapshot and negotiated storage capacity, including capacity reuse and single-slot transitions.

#### Scenario: Many maneuvers exceed the number of storage slots
- **WHEN** a route produces more maneuvers than the minimum capacity of the actual selected components
- **THEN** the sender SHALL reuse indices within that capacity according to the verified ordering contract
- **AND** actual receiver-parser tests SHALL check definition/reference/distance consistency

#### Scenario: Guidance ends without a confirmed arrival reason
- **WHEN** the source reports guidance ended but cannot distinguish cancellation from arrival
- **THEN** the publisher SHALL use the existing verified inactive/reset contract
- **AND** it SHALL NOT invent an arrival reason or revoke the receiver's subscription itself

### Requirement: Navigation text and overview fields keep their own source contracts

Current road, after-maneuver road, route distance, maneuver distance, time, ETA and lane fields SHALL retain distinct meanings. Text encoding, NUL and maximum-length measurement SHALL be established from evidence and declared capabilities before enabling an unverified field.

#### Scenario: A declared text limit has an unresolved measurement
- **WHEN** a target field has a declared limit but its byte/character measurement or source role is unresolved
- **THEN** the unresolved field SHALL remain disabled or retain its existing explicitly documented trial status
- **AND** a field name alone SHALL NOT justify truncation or unit conversion
